# 21Spring-WebCrawler



# UML



# Schema Design

[Alzconnected Discussion Board](https://www.alzconnected.org/discussion.aspx)

- **Forum**: <u>fid</u>, forum_heading,subforum_heading, forum_url topic_num, post_num, last_post_time, *last_post_uid(fk)*
- **Topic**: <u>tid</u>, *fid(fk)*, topic_url,topic_name, *topic_starter(fk)*, reply_num, view_num, last_post_time
- **Post**: <u>pid</u>, *tid(fk)*, is_reply, post_time, *post_author(fk)*

- **User**: <u>uid</u>, join_time, post_num, first_name, screen_name, location, birth_date, gender, relation_with_dementia, employment, children, maritial_status, notes

