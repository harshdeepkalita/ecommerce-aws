create table firehosetransactions(
	InvoiceNo varchar(200) not null,
	StockCode varchar(200) not null,
	Description varchar(200) not null,
	Quantity int not null,	
	InvoiceDate varchar(200) not null,
	UnitPrice float not null,
	CustomerID int not null,  	
 	Country varchar(200) not null
);
