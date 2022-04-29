-- Write a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and store
-- the average weighted score for a student.
-- Requirements:
--     Procedure ComputeAverageScoreForUser is taking 1 input:
--         user_id, a users.id value
--         (you can assume user_id is linked to an existing users)


DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id int
)
BEGIN
   UPDATE users SET average_score = (SELECT AVG(score)
    FROM corrections WHERE corrections.user_id=user_id
	GROUP BY corrections.user_id ) WHERE id=user_id;
END $$
DELIMITER;
