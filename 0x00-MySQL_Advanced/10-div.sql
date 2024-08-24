-- Creates a division function
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
RETURN IF(b = 0, 0, a/b)

