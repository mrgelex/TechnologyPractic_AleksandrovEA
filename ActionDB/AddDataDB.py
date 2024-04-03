import sqlite3 as sl
con = sl.connect('Logs.db')
with con:
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client1', '3', 'opi')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client2', '6', 'customer')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client3', '5', 'opi')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client4', '5', 'service')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client5', '8', 'customer')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client6', '8', 'customer')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client7', '3', 'customer')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client8', '4', 'opi')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client9', '5', 'service')""")
    con.commit()
    con.execute("""INSERT INTO CLIENTS (name, gmt, type) VALUES ('client10', '2', 'service')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('1', '0000000001', 'device01', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('1', '0000000002', 'device02', '9003')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('1', '0000000003', 'device03', '9003')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('2', '1111111110', 'device11', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('2', '1111111111', 'device11', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('2', '1111111112', 'device11', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('3', '2222222220', 'device21', '9002')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('3', '2222222221', 'device22', '9002')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('3', '2222222222', 'device23', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('4', '4444444440', 'device01', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('4', '4444444441', 'device02', '9000')""")
    con.commit()
    con.execute("""INSERT INTO DEVICES (id_client, name, username, version) VALUES ('5', '5555555550', 'device51', '9002')""")
    con.commit()
    