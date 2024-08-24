-- Calculates and stores a weighted average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
  DECLARE weighted_avg FLOAT;
  SELECT SUM(cor.score*proj.weight)/SUM(proj.weight) INTO weighted_avg
  FROM projects AS proj INNER JOIN corrections AS cor ON proj.id = cor.project_id
  WHERE cor.user_id = user_id;

  UPDATE users
  SET average_score = weighted_avg
  WHERE id = user_id;
END //

DELIMITER ;
