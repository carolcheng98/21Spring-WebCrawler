# Alzconnected Forum



# Data and Schema

### Forum:

- `forum.csv`: contains forum level data

  | Field          | Description                                          | Type   |
  | -------------- | ---------------------------------------------------- | ------ |
  | fid*           | forum id, retrieved from forum url                   | int    |
  | f_heading      | forum heading, the name of the forum                 | string |
  | f_subheading   | forum subheading, the brief description of the forum | string |
  | num_topics     | number of topics in the forum                        | int    |
  | last_post_date | last post day of the week, date, time                | string |
  | last_post_uid  | the user id of the last post author                  | int    |

### Topic:

- `topics_<FORUM_NAME>.csv`: contains topic level data

  | Field          | Description                                        | Type   |
  | -------------- | -------------------------------------------------- | ------ |
  | fid            | forum id, the id of the forum the topic belongs to | int    |
  | tid*           | topic id, retrieved from topic url                 | int    |
  | t_url          | url of the topic                                   | string |
  | t_heading      | topic heading, the title of the topic              | string |
  | num_replies    | number of replies to the topic                     | int    |
  | num_views      | number of views the topic received                 | int    |
  | starter_uid    | the user id of the topic starter                   | int    |
  | starter_name   | the username of the topic starter                  | string |
  | last_post_date | last post day of the week, date, time              | string |

### Post:

- ```posts_<TOPIC_NAME>.csv```: contains post level data

  | Field     | Description                                               | Type   |
  | --------- | --------------------------------------------------------- | ------ |
  | tid       | topic id, the id of the topic the post belongs to         | int    |
  | uid       | user id, the user id of the post creator                  | int    |
  | pid*      | post id, unique id for the post                           | int    |
  | p_content | post content                                              | string |
  | is_start  | 1 if the post is the first post of the topic, otherwise 0 | bool   |
  | p_date    | post day of the week, date, time                          | string |



### User:

- `user_all_forums.csv`: contains information of users from all forums

  - `user_caregiver_forum.csv`: contains information of users involved in the caregiver forum

  | Field     | Description                                | Type   |
  | --------- | ------------------------------------------ | ------ |
  | uid*      | user id                                    | int    |
  | username  | username                                   | string |
  | join_date | join date of the user                      | date   |
  | num_post  | the total number of posts the user creates | int    |
  |           |                                            |        |

## Script

- `run.py`: main program
  - multiprocessing enabled
  - save data to disk everytime the information of the posts in a topic is fetched
- `merge.py`: program to merge all pickle data
  - generate two csv files for posts and users

