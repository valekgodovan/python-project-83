DROP TABLE IF EXISTS urls;
CREATE TABLE urls
(
    id         bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name       VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP           NOT NULL DEFAULT CURRENT_TIMESTAMP
);
