-- Stored procedure that computes and stores the average score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (userID INT)
BEGIN
  DECLARE avg_score FLOAT;
  SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = userID;
  UPDATE users SET average_score = avg_score WHERE id = userID;
END //

DELIMITER ;