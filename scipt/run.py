import multiprocessing
import calendar
import time
import requests
import datetime
from bs4 import BeautifulSoup
from urllib import parse
import csv
import pandas as pd
import pickle

# get html code, convert to plaintext
def getHTML(url):
    r = requests.get(url,verify=False)
    #r.status_code
    plain=r.text
    s = BeautifulSoup(plain, 'html.parser')
    return s

def getForum(s):
    fields = ['fid', 'f_url','f_heading','f_subheading','num_topics','num_posts','last_post_date','last_post_uid']
    f_post=s.find_all('tr',{'class':'post'})
    rows = []
    for tags in f_post:
        link = tags.find_all('span',{'class':'forumheading'})[0]
        a = link.find_all('a')[0]
        fname = a.contents[0]
        url = a['href']
        fid = parse.parse_qs(parse.urlsplit(url).query)['f'][0]
        
        subheading = tags.find_all('span',{'class':'subforumheading'})[0].contents[0]
        topics = tags.find_all('td')[2].contents[0]
        posts = tags.find_all('td')[3].contents[0]
        last_date = tags.find_all('td')[4].contents[0]
        if last_date != '-':
            uid = parse.parse_qs(parse.urlsplit(tags.find_all('td')[4].contents[3]['data-remote']).query)['uid'][0]
        else:
            uid = '-'

        row = [fid, url, fname,subheading,topics,posts,last_date,uid]
        rows.append(row)

    return fields, rows

def getTopics(s, fid):
    fields = ['fid','tid','t_url','t_heading','num_replies','num_views','starter_uid','starter_name','last_post_date']
    rows = []
    postlst = s.find_all('tr',{'class':'post'})
    for post in postlst:
        # print('post: ', post)
        a = post.find_all('a')[0]
        # print('a:',a)
        tname = a.contents[0]
        url = a['href']
        # print('url: ', url)
        tid = parse.parse_qs(parse.urlsplit(url).query)['t'][0]

        uname = post.find_all('a')[1].contents[0]
        uid = parse.parse_qs(parse.urlsplit(post.find_all('a')[1]['data-remote']).query)['uid'][0]
        
        rep = post.find_all('td')[3].contents[0]
        view = post.find_all('td')[4].contents[0]
        date = post.find_all('td')[5].contents[0]
        
        row = [fid,tid,url,tname,rep,view,uid,uname,date]
        rows.append(row)
    return fields, rows

def crawlForumns():
    topsoup = getHTML('https://www.alzconnected.org/discussion.aspx')
    f_fields, f_rows = getForum(topsoup)
    writeToCSV(f_fields, f_rows,'forum.csv')
    return f_fields, f_rows
#f_fields, f_rows = crawlForumns()

def crawlTopicsbyForum(f_rows):
    for row in f_rows:
        print('getting info from forum: {}...'.format(row[2]))
        rows = []
        i = 1
        while True:
            forumURL = "https://www.alzconnected.org{}&page={}".format(row[1],i)
            s = getHTML(forumURL)
            fields, cur_row = getTopics(s,row[0])
            if len(cur_row)==0:
                print('Done with forum: {}.'.format(row[2]))
                break
            else:
                if i % 10 == 0:
                    print('Successfully getting info from {} page {}'.format(row[2],i))
                rows.extend(cur_row)
                i+=1
        writeToCSV(fields, rows, 'topics_{}.csv'.format(row[2]))
#crawlTopicsbyForum(f_rows)

def getPostsAndUser(s, tid):
    post_fields = ['tid', 'uid','pid','p_content','is_start','p_date']
    user_fields = ['uid','username','join_date','num_post']
    postlst = s.find_all('tr',{'class':'post'})
    userlst = s.find_all('tr',{'class':'postheader'})
    
    assert len(postlst) == len(userlst)
    posts = []
    user_dict = {}

    for i in range(len(userlst)):
        user = userlst[i]
        post = postlst[i]

        isStart = True if i == 0 else False
        pid = user.find_all('a')[0]['name'][5:]
        try:
            uid = parse.parse_qs(parse.urlsplit(user.find_all('a')[1]['data-remote']).query)['uid'][0] if i!=len(userlst)-1 else parse.parse_qs(parse.urlsplit(user.find_all('a')[2]['data-remote']).query)['uid'][0]
            uname = user.find_all('a')[1].contents[0] if i!=len(userlst)-1 else user.find_all('a')[2].contents[0]
            dp = post.find_all('td',{'class':'UserBox'})[0].text.split('Joined: ',1)[1]
            dp = dp.split('Posts: ')
            join_date = dp[0]
            post_num = [int(s) for s in dp[1].split() if s.isdigit()][0]
        except IndexError:
            print('post id {} can\'t get user information'.format(pid))
            uid = 0 
            uname = 0
            join_date = 0
            post_num = 0

        msg = post.find_all('td',{'class':'message ekMessage'})[0]
        content = msg.text
        p_date=user.find_all('td',{'class':'postheader'})[0].text.split('\t')[-4]

        post = [tid, uid,pid,content,isStart,p_date]
        posts.append(post)
        user_dict[uid] = [uid, uname, join_date, post_num]
    return post_fields, user_fields, posts, user_dict

def getPostsbyForum(idx,tid):
    print("Start fetching {}".format(tid))
    url = 'https://www.alzconnected.org/discussion.aspx?g=posts&t={}'.format(tid)
    soup = getHTML(url)
    post_fields, user_fields, posts, user_dict = getPostsAndUser(soup,tid)
    pickle.dump((posts, str(user_dict)),open("posts-20000-25000/{}.pkl".format(idx),"wb"))
    print("Done id {}".format(idx),flush=True)

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == "__main__":
    start_time = time.time()
    pool = multiprocessing.Pool()

    forum_lst = ['Caregivers Forum']
    for forum_name in forum_lst:
        print('Getting post info from {}...'.format(forum_name))
        df = pd.read_csv('topics_{}.csv'.format(forum_name))
        print(len(df.tid))
        tids = df.tid[20000:25000]

        print("# tids: ",len(tids))
        for idx, tid in enumerate(tids):
            pool.apply_async(getPostsbyForum,args=(idx,tid,))

    pool.close()
    pool.join()
    end_time = time.time()
    print("Time: {}s".format(end_time - start_time))