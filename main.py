#The procedure we follow to connect Flask-MySQL is as follows:
import json
from flask import Flask , jsonify ,request
from flask_mysqldb import MySQL
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

app.config["DEBUG"] = True
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '01233210'       ##########Note that: this should be changed according to your mysql root's password

#the name of the database :)
app.config['MYSQL_DB'] = 'onlinestore'

mysql = MySQL(app)
parser = reqparse.RequestParser()

def ConvertTupleToJson(cursor,tuple):
    field_names = [i[0] for i in cursor.description]
    #because tuple is (())
    tuple = tuple[0]
    d = {}
    for i in range(len(field_names)):
        d[field_names[i]] = tuple[i]
    json_string = json.dumps(d)
    return json_string

####################################### Building our restful api ##################################

class login_getCustomer(Resource):
    def post(self):
        try:
            parser.add_argument("Email")
            parser.add_argument("Password")
            args = parser.parse_args()

            cursor = mysql.connection.cursor()
            query_getCustomerIdWithEmailAndPassword = " Select * From customer where Email = '{}' and Password = '{}'; ".format(args["Email"],args["Password"])
            cursor.execute(query_getCustomerIdWithEmailAndPassword)
            customerData = cursor.fetchall()
            mysql.connection.commit()
        except:
            cursor.close()
            return None
        if(customerData==()):
            # no matching email and password (If customer credentials are invalid!)
            cursor.close()
            return None
        else:
            cursor.close()
            return ConvertTupleToJson(cursor,customerData)


class signup_addCustomer(Resource):
    def post(self):
        try:
            parser.add_argument("FirstName")
            parser.add_argument("SecondName")
            parser.add_argument("PhoneNumber")
            parser.add_argument("Gender")
            parser.add_argument("Email")
            parser.add_argument("Password")
            parser.add_argument("Governorate")
            parser.add_argument("City")
            parser.add_argument("StreetName")
            parser.add_argument("BuildingNumber")
            parser.add_argument("AppartmentNumber")

            args = parser.parse_args()
            cursor = mysql.connection.cursor()
            query_insertCustomer = " insert into customer (FirstName,SecondName,Governorate,City,StreetName,BuildingNumber,AppartmentNumber,Gender,PhoneNumber,Email,Password) values ('{}','{}','{}','{}','{}',{},{},'{}',{},'{}','{}');".format(args["FirstName"] , args["SecondName"] , args["Governorate"] , args["City"] , args["StreetName"] , args["BuildingNumber"] , args["AppartmentNumber"] , args["Gender"] , args["PhoneNumber"] , args["Email"], args["Password"])
            cursor.execute(query_insertCustomer)
            query_getCustomerWithEmail = "select * from customer where Email = '{}'".format(args["Email"])
            cursor.execute(query_getCustomerWithEmail)
            customerData = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
        except:
            #an exception will be thrown if phoneNum or email or both are duplicated (If customer is already signed up (registered))
            cursor.close()
            return None
        #cursor.fetchall() returns a table (i.e. [[val_1,val_2,....,val_lastAttribute]] )
        return ConvertTupleToJson(cursor,customerData)

class signup_addEmployee(Resource):
    def post(self):
        try:
            parser.add_argument("FirstName")
            parser.add_argument("SecondName")
            parser.add_argument("PhoneNumber")
            parser.add_argument("Email")
            parser.add_argument("Password")
            parser.add_argument("Position")
            parser.add_argument("Governorate")
            parser.add_argument("City")
            parser.add_argument("StreetName")
            parser.add_argument("BuildingNumber")
            parser.add_argument("AppartmentNumber")

            args = parser.parse_args()
            cursor = mysql.connection.cursor()

            query_insertEmployee = " insert into {} (FirstName,SecondName,Governorate,City,StreetName,BuildingNumber,AppartmentNumber,PhoneNumber,Email,Password) values ('{}','{}','{}','{}','{}',{},{},{},'{}','{}');".format(args["Position"],args["FirstName"] , args["SecondName"] , args["Governorate"] , args["City"] , args["StreetName"] , args["BuildingNumber"] , args["AppartmentNumber"] , args["PhoneNumber"] , args["Email"], args["Password"])
            cursor.execute(query_insertEmployee)
            query_getEmployeeWithEmail = "select * from {} where Email = '{}'".format(args["Position"], args["Email"])
            cursor.execute(query_getEmployeeWithEmail)
            employeeData = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
        except:
            #an exception will be thrown if phoneNum or email or both are duplicated (If employee is already signed up (registered))
            cursor.close()
            return None
        #cursor.fetchall() returns a table (i.e. [[id]] ) thats why we return [0][0]
        return ConvertTupleToJson(cursor,employeeData)


class login_getEmployee(Resource):
    def post(self):
        try:
            parser.add_argument("Email")
            parser.add_argument("Password")
            parser.add_argument("Position")

            args = parser.parse_args()

            cursor = mysql.connection.cursor()
            query_getEmployeeWithEmailAndPassword = " Select * From {} where Email = '{}' and Password = '{}'; ".format(args["Position"],args["Email"],args["Password"])
            cursor.execute(query_getEmployeeWithEmailAndPassword)
            employeeData = cursor.fetchall()
            mysql.connection.commit()
        except:
            cursor.close()
            return None
        if (employeeData == ()):
            # no matching email and password (If customer credentials are invalid!)
            cursor.close()
            return None
        else:
            cursor.close()
            return ConvertTupleToJson(cursor, employeeData)


api.add_resource(signup_addCustomer,'/addCustomer')
api.add_resource(signup_addEmployee,'/addEmployee')
api.add_resource(login_getCustomer,'/getCustomer')
api.add_resource(login_getEmployee,'/getEmployee')


if __name__ == '__main__':
    app.run(debug=True)
