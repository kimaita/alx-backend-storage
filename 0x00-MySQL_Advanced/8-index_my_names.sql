-- Creates an index in names for the column name's first letter
CREATE INDEX name_lttr_idx ON names (name(0));

