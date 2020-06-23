from mysql.connector import connect
import file_logs
import connection


class EmployeeSwipe:
    def __init__(self):
        try:
            f = file_logs.FileLog(__name__)
            self.logger = f.logs_handler("Swipe Entry")
            d = connection.DevConfig(self.logger)
            host, user, password, database = d.connect_db()
            self.db = connect(host=host, user=user, password=password, db=database)
            self.logger.info("Database Connection Established {}@{} with password {}".format(user, host,
                                                                                             '*' * len(password)))
        except Exception as e:
            print(e)
            self.logger.exception("Exception occurred!!!!!", e)

    def in_out_calc(self, year):
        try:
            cursor = self.db.cursor()
            if 2017 < year < 2020:
                query1 = 'select id,sec_to_time(avg(time_to_sec(out_time)-time_to_sec(in_time))) as avg_time_in_month' \
                         ' from swipe where year(swipe_date) = {} group by month(swipe_date);'
                cursor.execute(query1.format(year))
                result_set = cursor.fetchall()
                print('Average time in office:')
                for i in result_set:
                    print(i)

            query2 = 'select id,count(id) as days_left_earlier from swipe ' \
                     'where time_to_sec(out_time) < time_to_sec(\'17:00:00\') group by id;'
            print('Employee who left early and the no of days left earlier:')
            cursor.execute(query2)
            result_set = cursor.fetchall()
            for i in result_set:
                print(i)
        except Exception as e:
            print(e)
            self.logger.exception("Exception occurred!!!!!", e)


if __name__ == '__main__':
    s = EmployeeSwipe()
    y = int(input('Enter the year(2018 or 2019):'))
    s.in_out_calc(y)
