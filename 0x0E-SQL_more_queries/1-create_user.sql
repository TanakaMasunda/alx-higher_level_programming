-- create MySQL servr usr(user_0d_1.)wth(all privileges,user_0d_1_pwd as pswd)
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEDGES ON * . * TO user_0d_1@localhost;
