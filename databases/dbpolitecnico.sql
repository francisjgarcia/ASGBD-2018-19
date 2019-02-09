--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: tbalumnos_id; Type: SEQUENCE; Schema: public; Owner: frodo
--

CREATE SEQUENCE public.tbalumnos_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbalumnos_id OWNER TO frodo;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: tbalumnos; Type: TABLE; Schema: public; Owner: frodo
--

CREATE TABLE public.tbalumnos (
    id integer DEFAULT nextval('public.tbalumnos_id'::regclass) NOT NULL,
    nombre character varying(25),
    edad integer
);


ALTER TABLE public.tbalumnos OWNER TO frodo;

--
-- Data for Name: tbalumnos; Type: TABLE DATA; Schema: public; Owner: frodo
--

COPY public.tbalumnos (id, nombre, edad) FROM stdin;
1	Francis	24
2	Edu	21
\.


--
-- Name: tbalumnos_id; Type: SEQUENCE SET; Schema: public; Owner: frodo
--

SELECT pg_catalog.setval('public.tbalumnos_id', 13, true);


--
-- Name: tbalumnos tbalumnos_pkey; Type: CONSTRAINT; Schema: public; Owner: frodo
--

ALTER TABLE ONLY public.tbalumnos
    ADD CONSTRAINT tbalumnos_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

