

SET row_security = off;

INSERT INTO public.user("user_id", "email", "name", "display_id") VALUES (1, 'user1@test.com', 'user 1', 'u1');
INSERT INTO public.user("user_id", "email", "name", "display_id") VALUES (2, 'user2@test.com', 'user 2', 'u2');
INSERT INTO public.user("user_id", "email", "name", "display_id") VALUES (3, 'user3@test.com', 'user 3', 'u3');

INSERT INTO public.address("address_id", "is_primary", "user_id", "address_line1", "address_line2") VALUES (1, FALSE, 1, '1 Fake St', 'Suburb 1');
INSERT INTO public.address("address_id", "is_primary", "user_id", "address_line1", "address_line2") VALUES (2, TRUE, 1, '2 Fake St', 'Suburb 2');
INSERT INTO public.address("address_id", "is_primary", "user_id", "address_line1", "address_line2") VALUES (3, FALSE, 2, '3 Fake St', 'Suburb 3');

