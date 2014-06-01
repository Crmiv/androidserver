create table userinfo(
		id int unsigned not null auto_increment primary key,
		cutename char(30) not null,
		username char(30) not null,
		password char(18) not null,
		sex char(2) not null,
		years int unsigned not null,
		create_date date not null,
		edit_date date not null,
		login_date date 
		);

/*create user*/
INSERT INTO userinfo (id,user,password,sex,years,time) values ('',
	user_,password_,sex_,years_,CURRENT_DATE);
/*delete user*/
delete from userinfo where user = user_;
/*edit user info */
{
	update userinfo set cutename = _cutename where user = user_;
	update userinfo set edit_date = CURRENT_DATE where user = user_;
	}
/*
 edit password
 */
{
update userinfo set password = _password where user = user_;
update userinfo set edit_date = CURRENT_DATE where user = user_;
}

/*frnd complex name is frnd + 'id_'*/
create table frnd(
		id int unsigned not null,
		frndnum int unsigned not null auto_increment primary key,
		frndid int unsigned not null
		)

/*add friend*/
	INSERT INTO frnd (id, frndnum, frndid) values (id_,'',frndid_);
/*count friend number*/
	SELECT MAX(frndnum) FROM frnd.id = id_;
/*delete friend*/
/*IMPORTANT!
friend-relationship have duality*/
	DELETE FROM frnd WHERE frndid = _frndid;

/*create feeling table,and complex name is feeling + 'id_'*/
create table feeling(
		id int unsigned not null,
		feelingnum int unsigned not null auto_increment primary key,
		text varchar(108) not null,
		image char(100) ,
		video char(100),
		add_time time not null
		);

/*add feeling*/
	INSERT INTO feeling (id, feelingnum, text, image, video, add_time) values (
		_id, '', _text, _image, _video, CURRENT_TIME);
/*delete feeling*/
	DELETE FROM feeling WHERE feelingnum = _feelingnum;

/*create feelingcomment,complex name is feelingcomment + 'id_' + 'feelingnum_'*/
create table feelingcomment(
		id int unsigned not null,
		feelingnum int unsigned not null,
		commentid int unsigned not null auto_increment primary key,
		commentfrom int unsigned not null,
		text varchar(108) not null,
		comment_time time not null
		);

/*add feelingcomment*/
	INSERT INTO feelingcomment (id, feelingnum, commentid, commentfrom, text, 
		comment_time) values (_id, _feelingnum, '', _commentfrom, _text, CURRENT_TIME);

/*delete feelingcomment*/
	DELETE FROM feeling WHERE commentid = _commentid;

	
/*COMPLEX OPERATION
 NEXT->
 */








