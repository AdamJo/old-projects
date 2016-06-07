create table "forrent" ( 
        apartment_name varchar(128) PRIMARY KEY, 
        street_address varchar(128), 
        city varchar(64), 
        state varchar(2), 
        zip_code varchar(16), 
        postal_address varchar(128),
        phone_number varchar(16), 
        link varchar(128), 
        latitude varchar(32), 
        longitude varchar(32), 
        date_added date not null default CURRENT_DATE
)