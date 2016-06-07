CREATE TABLE "forrent_prices" ( 
	apartment_name varchar references forrent(apartment_name),
	layout varchar (32),
	price int,
            date_added date not null default CURRENT_DATE
);
