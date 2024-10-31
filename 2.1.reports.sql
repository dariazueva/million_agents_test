CREATE TABLE reports
(
    id int PRIMARY KEY,
    user_id int,
    reward int,
    created_at timestamp without time zone
);

INSERT INTO reports (user_id, reward, created_at) VALUES
    (1, 100, '2021-03-15 10:00:00'),
    (1, 150, '2022-05-20 14:30:00'),
    (1, 200, '2022-11-25 09:00:00'),
    (2, 120, '2020-08-10 08:15:00'),
    (2, 130, '2022-02-17 11:45:00'),
    (3, 140, '2021-06-05 12:00:00'),
    (3, 160, '2022-09-22 16:30:00'),
    (4, 110, '2022-01-15 10:00:00'),
    (5, 90, '2021-10-30 09:00:00'),
    (5, 200, '2022-03-18 10:30:00');

SELECT user_id, SUM(reward) AS total_reward_2022
FROM reports
WHERE created_at >= '2022-01-01' AND created_at < '2023-01-01'
  AND user_id IN (
    SELECT user_id
    FROM reports
    WHERE created_at >= '2021-01-01' AND created_at < '2022-01-01'
    GROUP BY user_id
    HAVING MIN(created_at) >= '2021-01-01' AND MIN(created_at) < '2022-01-01'
)
GROUP BY user_id;