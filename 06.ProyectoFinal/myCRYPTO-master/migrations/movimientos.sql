BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "cryptos" (
	"Id"	INTEGER,
	"clave"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "movements" (
	"Id"	INTEGER,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"moneda_from"	TEXT NOT NULL,
	"cantidad_from"	REAL NOT NULL,
	"moneda_to"	TEXT NOT NULL,
	"cantidad_to"	REAL NOT NULL,
	FOREIGN KEY("moneda_to") REFERENCES "cryptos"("Id"),
	FOREIGN KEY("moneda_from") REFERENCES "cryptos"("Id")
	PRIMARY KEY("Id" AUTOINCREMENT)
);
INSERT INTO "cryptos" VALUES (1,'EUR','EURO'),
 (2,'BTC','Bitcoin'),
 (3,'ETH','Ether'),
 (4,'XRP','Ripple'),
 (5,'LTC','Litecoin'),
 (6,'BCH','Bitcoin Cash'),
 (7,'BNB','Binance Coin'),
 (8,'USDT','Tether'),
 (9,'EOS','EOS'),
 (10,'BSV','Bitcoin SV'),
 (11,'XLM','Stellar'),
 (12,'ADA','Cardano'),
 (13,'TRX','TRON');
COMMIT;