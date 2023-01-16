-- Table: public.Population

-- DROP TABLE IF EXISTS public."Population";

CREATE TABLE IF NOT EXISTS public."Population"
(
    region integer,
    year integer NOT NULL,
    gender "char",
    age "char"[],
    count integer,
    CONSTRAINT "Population_pkey" PRIMARY KEY (year)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Population"
    OWNER to postgres;
	
	
-- Table: public.Region

-- DROP TABLE IF EXISTS public."Region";

CREATE TABLE IF NOT EXISTS public."Region"
(
    code integer,
    name "char"[]
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Region"
    OWNER to postgres;
	
	
-- Table: public.Time_series_info

-- DROP TABLE IF EXISTS public."Time_series_info";

CREATE TABLE IF NOT EXISTS public."Time_series_info"
(
    year integer NOT NULL,
    martality_rate real,
    mid_salary_uah real,
    "GDP" real,
    fertility_rate real,
    CONSTRAINT "Time_series_info_pkey" PRIMARY KEY (year)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Time_series_info"
    OWNER to postgres;