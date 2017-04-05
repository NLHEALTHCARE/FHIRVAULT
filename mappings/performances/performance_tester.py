""" Performance vergelijken tussen queries op gewone tabellen ("gewoon") en jsonb tabellen ("jsonb") met exact dezelfde data, maar dan in een jsonb veld

!!! run peformance_proces.py eerst zodat sor_test.performgewoon_100_hstage en varianten erop bestaan.
"""
from mappings.performances.performance_mappings import execute_sql, execute_sql2
import timeit
import time
from functools import wraps
import datetime


# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         r = func(*args, ** kwargs)
#         end = time.perf_counter()  # http://stackoverflow.com/questions/25785243/understanding-time-perf-counter-and-time-process-time
#         # print('[].{}: {}'.format(func.__module, func.__name__, end - start))
#         print('{}: {}'.format(func.__name__, end - start))
#         return r
#     return wrapper


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        # print("start: ", start)
        r = func(*args, ** kwargs)
        end = datetime.datetime.now()  # http://stackoverflow.com/questions/25785243/understanding-time-perf-counter-and-time-process-time
        # print("end: ", end)
        # print('[].{}: {}'.format(func.__module, func.__name__, end - start))
        print('{}: {}'.format(func.__name__, end - start))
        return r
    return wrapper


############################
# SQL voor gewone tabellen #
############################

@timethis
def init_performtester_gewoon_tabel():
    sql = """
    DROP TABLE if exists sor_test.performtester_gewoon;

    CREATE TABLE sor_test.performtester_gewoon(
	  id SERIAL PRIMARY KEY,
	  waarde1 TEXT NOT NULL,
	  waarde2 TEXT NOT NULL,
	  waarde3 TEXT NOT NULL
	);
    """
    execute_sql(sql)


@timethis
def insert_gewoon100():
    sql = """
	insert into sor_test.performtester_gewoon (waarde1, waarde2, waarde3)
    select waarde1, waarde2, waarde3
    from sor_test.performgewoon_100_hstage;
    """
    execute_sql(sql)


@timethis
def insert_gewoon1mil():
    sql = """
	insert into sor_test.performtester_gewoon (waarde1, waarde2, waarde3)
    select waarde1, waarde2, waarde3
    from sor_test.performgewoon_1miljoen_hstage;
    """
    execute_sql(sql)


@timethis
def insert_gewoon10mil():
    sql = """
	insert into sor_test.performtester_gewoon (waarde1, waarde2, waarde3)
    select waarde1, waarde2, waarde3
    from sor_test.performgewoon_10miljoen_hstage;
    """
    execute_sql(sql)


@timethis
def insert_gewoon10x1mil():
    for i in range (10):
        insert_gewoon1mil()


@timethis
def select_gewoon_specwaarde1(int):

    sql= """
    SELECT id, waarde1
    from sor_test.performtester_gewoon
    WHERE id = {};""".format(int)
    result = execute_sql2(sql)
    waarde = result[0][1]

    # print(result)
    return waarde


@timethis
def select_gewoon_results(waarde):

    sql= """
    SELECT id, waarde2, waarde3
    from sor_test.performtester_gewoon
    WHERE waarde1 = '{}';""".format(waarde)
    result = execute_sql2(sql)

    return result


@timethis
def select_like_gewoon(substring):
    sql = """
    SELECT waarde1, waarde2, waarde3
    FROM sor_test.performtester_gewoon
    WHERE waarde1 LIKE '%{}%';""".format(substring)
    result = execute_sql2(sql)
    return result


@timethis
def update_like_gewoon(substring):
    sql = """UPDATE FROM sor_test.performtester_gewoon
    SET waarde1 = 'bevatte een 4'
    where waarde1 in (SELECT waarde1
                      FROM sor_test.performtester_gewoon
                      WHERE waarde1 LIKE '%{}%');""".format(substring)
    execute_sql(sql)

@timethis
def delete_like_gewoon(substring):
    sql = """
    DELETE FROM sor_test.performtester_gewoon
    where waarde1 in (SELECT waarde1
                      FROM sor_test.performtester_gewoon
                      WHERE waarde1 LIKE '%{}%')
    """.format(substring)
    execute_sql(sql)


@timethis
def join_gewoon():
    sql = """
    SELECT  h.waarde1 as waarde1_100, m.waarde1 as waarde1_1miljoen
    FROM sor_test.performgewoon_100_hstage h, sor_test.performgewoon_1miljoen_hstage m
    where h.id = m.id;"""
    execute_sql(sql)


###########################
# SQL voor JSONB tabellen #
###########################


def init_performtester_jsonb_tabel():
    sql = """
    DROP TABLE if exists sor_test.performtester_jsonb;

    CREATE TABLE sor_test.performtester_jsonb(
	  id SERIAL PRIMARY KEY,
	  details jsonb not NULL
	);
    """
    execute_sql(sql)


@timethis
def insert_jsonb100():
    sql = """
	insert into sor_test.performtester_jsonb (details)
    select details
    from sor_test.performjsonb_100_hstage;
    """
    execute_sql(sql)


@timethis
def insert_jsonb1mil():
    sql = """
	insert into sor_test.performtester_jsonb (details)
    select details
    from sor_test.performjsonb_1miljoen_hstage;
    """
    execute_sql(sql)


@timethis
def insert_jsonb10mil():
    sql = """
	insert into sor_test.performtester_jsonb (details)
    select details
    from sor_test.performjsonb_10miljoen_hstage;
    """
    execute_sql(sql)


@timethis
def insert_jsonb10x1mil():
    for i in range (10):
        insert_jsonb1mil()


@timethis
def select_jsonb_specwaarde1(int):

    sql= """
    SELECT id, details->>'waarde1'
    from sor_test.performtester_jsonb
    WHERE id = {};""".format(int)
    result = execute_sql2(sql)
    waarde = result[0][1]

    # print(result)
    return waarde


@timethis
def select_jsonb_results(waarde):

    sql= """
    SELECT id, details->>'waarde2' as waarde2, details->>'waarde3' as waarde3
    from sor_test.performtester_jsonb
    WHERE details->'waarde1' ? '{}';""".format(waarde)
    result = execute_sql2(sql)

    return result


@timethis
def select_like_jsonb(substring):
    sql = """
    SELECT details
    FROM sor_test.performtester_jsonb
    WHERE details->>'waarde1' LIKE '%{}%';""".format(substring)
    result = execute_sql2(sql)
    return result





@timethis
def delete_like_jsonb(substring):
    sql = """
    DELETE
    FROM sor_test.performtester_jsonb
    WHERE details in ((SELECT details
                    FROM sor_test.performtester_jsonb
                    WHERE details->>'waarde1' LIKE '%{}%'))
    ;""".format(substring)

    execute_sql(sql)


@timethis
def array_to_json100():

    sql = """
    DROP TABLE if exists sor_test.performtester_json_array;

    CREATE TABLE sor_test.performtester_json_array(
	  id SERIAL PRIMARY KEY,
	  details json not NULL
	);

    insert into sor_test.performtester_json_array (details)
    VALUES
          ((SELECT array_to_json(array_agg(row_to_json(t)), true)
            FROM
                (SELECT waarde1, waarde2, waarde3 FROM sor_test.performgewoon_100_hstage) as t));"""
    execute_sql(sql)


@timethis
def array_to_json1mil():

    sql = """
    DROP TABLE if exists sor_test.performtester_json_array;

    CREATE TABLE sor_test.performtester_json_array(
	  id SERIAL PRIMARY KEY,
	  details json not NULL
	);

    insert into sor_test.performtester_json_array (details)
    VALUES
          ((SELECT array_to_json(array_agg(row_to_json(t)), true)
            FROM
                (SELECT waarde1, waarde2, waarde3 FROM sor_test.performgewoon_1miljoen_hstage) as t));"""
    execute_sql(sql)


@timethis
def join_jsonb():
    sql = """
    SELECT  h.details as details1_100, m.details as details_1miljoen
    FROM sor_test.performjsonb_100_hstage h, sor_test.performjsonb_1miljoen_hstage m
    where h.id = m.id"""
    execute_sql(sql)





#####################################################################################################################################################################

""" test of een insert verandert bij steeds groter wordende tabellen:  (kijk of @timethis actief is of niet voor "insert_gewoon1mil()" en "insert_jsonb1mil()") """

# print("verandert de hoeveelheid benodigde tijd wanneer er vaker een insert gedaan wordt?")
# counter = 0
# while counter < 5:
#     init_performtester_gewoon_tabel()
#     # insert_gewoon100()
#     insert_gewoon1mil()
#     insert_gewoon1mil()
#     insert_gewoon1mil()
#     insert_gewoon1mil()
#     insert_gewoon1mil()
#     counter += 1
#
#
# counter = 0
# while counter < 5:
#     init_performtester_jsonb_tabel()
#     # insert_jsonb100()
#     insert_jsonb1mil()
#     insert_jsonb1mil()
#     insert_jsonb1mil()
#     insert_jsonb1mil()
#     insert_jsonb1mil()
#
#     counter += 1
#

# """ testen of het beter is om 10x 1miljoen rijen te inserten of 1x 10 miljoen rijen (check of de @timethis actief zijn"""
#
# print("Testen of het beter is om 10x 1miljoen rijen te inserten of 1x 10 miljoen rijen: \n")
#
# init_performtester_gewoon_tabel()
# insert_gewoon10mil()
#
# init_performtester_gewoon_tabel()
# insert_gewoon10x1mil()
#
# init_performtester_jsonb_tabel()
# insert_jsonb10mil()
#
# init_performtester_jsonb_tabel()
# insert_jsonb10x1mil()
#
#
# """ select statements testen"""
#
# print("select statements testen:")
# print("")
# print("")
#
print("Gewone variant:")
print("")

init_performtester_gewoon_tabel()
# insert_gewoon10mil()
init_performtester_gewoon_tabel()
insert_gewoon1mil()
# waarde = select_gewoon_specwaarde1(99)
waarde = select_gewoon_specwaarde1(999999)
select_gewoon_results(waarde)
result = select_like_gewoon('4')
update_like_gewoon('4')
delete_like_gewoon('4')

print("")
print("Jsonb variant:")
print("")


init_performtester_jsonb_tabel()
insert_jsonb1mil()
waarde = select_jsonb_specwaarde1(999999)
select_jsonb_results(waarde)
result = select_like_jsonb('4')
delete_like_jsonb('4')  # dit duurt exteem lang indien de tabel uit 10 miljoen rijen bestaat
#
#
# """ conversie naar een array   """
#
# print("")
# print("conversie naar een array\n")
#
#
# array_to_json100()
# array_to_json1mil()  # deze werkt maar duurt heel lang voor dit de resultaat tabel geladen is om te bekijken. Niet praktisch dus
# ## array_to_json10mil() resulteert in: "psycopg2.OperationalError: array size exceeds the maximum allowed (1073741823)"
#
#
# """ testen van joinen"""
#
# print("")
# print("testen van joinen\n")
# join_gewoon()
# join_jsonb()