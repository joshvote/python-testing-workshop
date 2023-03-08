

SET row_security = off;

INSERT INTO public.user("user_id", "email", "name", "display_id") VALUES (1, 'user1@test.com', 'user 1', 'u1');
INSERT INTO public.user("user_id", "email", "name", "display_id") VALUES (2, 'user2@test.com', 'user 2', 'u2');
INSERT INTO public.user("user_id", "email", "name", "display_id") VALUES (3, 'user3@test.com', 'user 3', 'u3');

INSERT INTO public.address("address_id", "address", "is_primary", "user_id") VALUES (1, '1 Fake St', FALSE, 1);
INSERT INTO public.address("address_id", "address", "is_primary", "user_id") VALUES (2, '2 Fake St', TRUE, 1);
INSERT INTO public.address("address_id", "address", "is_primary", "user_id") VALUES (3, '3 Fake St', FALSE, 2);

