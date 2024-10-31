CREATE TABLE pos
(
    id int PRIMARY KEY,
    title character varying
);

CREATE TABLE reports
(
    id int PRIMARY KEY,
    barcode character varying,
    price float,
    pos_id int
);

INSERT INTO pos (title) VALUES
    ('Store A'),
    ('Store B'),
    ('Store A'),
    ('Store C');

INSERT INTO reports (barcode, price, pos_id) VALUES
    ('123456', 10.99, 1),
    ('234567', 12.49, 1),
    ('345678', 8.99, 2),
    ('456789', 15.99, 3),
    ('123456', 11.49, 4),
    ('234567', 13.99, 4);

SELECT r.barcode, r.price
FROM reports r
         JOIN pos p ON r.pos_id = p.id
WHERE p.title IN (
    SELECT title
    FROM pos
    GROUP BY title
    HAVING COUNT(*) > 1
)
ORDER BY r.barcode;