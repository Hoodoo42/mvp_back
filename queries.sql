CALL gamer_signup('user4', 'pass4', '42389479237'); 
CALL gamer_login('user1', 'pass1', '213984729874');
CALL gamer_get(4);
CALL gamer_logout('42389479237');
CALL get_gamer(5);

CALL points_get ();
CALL points_update (13, 5);