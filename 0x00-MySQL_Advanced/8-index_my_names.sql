-- Creates an index in names for the column name's first letter
CREATE INDEX idx_name_first ON names (name(1));

