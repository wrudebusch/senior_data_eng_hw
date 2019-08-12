William Rudebusch 
Aug 12, 2019

#Answer the following questions (please provide the answer and the SQL used to get that answer):

##1. What is the number of unique users?
2904

```SELECT COUNT(DISTINCT user_id) FROM users WHERE user_id IS NOT NULL;```

##2. Who are the marketing ad providers?
 provider  | count 
-----------+-------
           |     1
 Instagram |  1811
 Facebook  |  1723
 Inst      |     1 <- suspect
 Snapchat  |  1861
 325       |     1 <- error
 Spotify   |  1790

```SELECT provider, COUNT(*) FROM marketing GROUP BY provider;```


##3. Which user property is changed the most frequently?
drinking

```SELECT COUNT(*), property FROM users GROUP BY property ORDER BY COUNT DESC;```


##4. Which ad was showed the most to users who identify as moderates?
NOTE: I answered "who has _ever_ identified as moderate" since _currently_ identify as moderate would be a little tricky. 
ad_id = 4

 ```SELECT m.ad_id, COUNT(*) FROM users AS u 
 	JOIN marketing AS m ON m.phone_id = u.phone_id 
 	WHERE u.property = 'politics' AND u.value = 'Moderate' 
 	GROUP BY  m.ad_id ORDER BY COUNT DESC;```

##5. What are the top 5 ads? Explain how you arrived at that conclusion.
top five are 1,4,2,0,3
 ad_id  | count 
--------+-------
 1      |   745
 4      |   731
 2      |   689
 0      |   673
 3      |   673

```mytestdb=# SELECT ad_id, COUNT(*) FROM marketing GROUP BY ad_id ORDER BY COUNT DESC;```