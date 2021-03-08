import pickle
import csv
import os

def writeToCSV(field, rows, fname):
    with open(fname, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(field)
        csvwriter.writerows(rows)

forum_posts = []
posts_fields = ['tid', 'uid','pid','p_content','is_start','p_date']
user_all = {}

folders = ["posts-0-5000","posts-5000-10000",
"posts-10000-15000","posts-15000-20000","posts-20000-25000","posts-30000","posts-25000-30000"]
print("Start merging...")
for folder in folders:
    print('merging folder {}'.format(folder))
    for i in range(5000):
        if not os.path.isfile("{}/{}.pkl".format(folder,i)):
            continue
        with open("{}/{}.pkl".format(folder,i),"rb") as infile:
            posts, user_dict = pickle.load(infile)
            user_dict = eval(user_dict)
            forum_posts.extend(posts)
            user_all = {**user_all, **user_dict}
        if (i+1) % 100 == 0:
            print("Done {} / 5000".format(i+1))

print('Done merging, total posts: {}'.format(len(forum_posts)))
writeToCSV(posts_fields, forum_posts, 'posts_{}.csv'.format("Caregivers Forum"))

user_fields = ['uid','username','join_date','num_post']
users = list(user_all.values())
print('number of users: ', len(users))
writeToCSV(user_fields, users, 'user_caregiver.csv')