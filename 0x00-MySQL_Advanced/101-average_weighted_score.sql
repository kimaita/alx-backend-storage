-- Calculates and stores a weighted average score for each student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  INSERT INTO users (id, name, average_score)
    SELECT * FROM
    (SELECT cor.user_id, '', SUM(cor.score*proj.weight)/SUM(proj.weight) AS weighted_avg
    FROM projects AS proj INNER JOIN corrections AS cor ON proj.id = cor.project_id
    GROUP BY user_id) AS wghtd
  ON DUPLICATE KEY UPDATE average_score = weighted_avg;
END //

DELIMITER ;
