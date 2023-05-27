CREATE TABLE "user" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"height"	REAL,
	"created"	DATETIME NOT NULL,
	"deleted"	BOOL,
	PRIMARY KEY("id" AUTOINCREMENT)
);