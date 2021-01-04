import 'dart:convert';
import 'package:http/http.dart' as http;
//don't forget to include in the pubspec.yaml: http: ^0.12.0+2

class URLS {
  //This stores the url that we'll deal with the restful api through
  //for web-based applications this will be http://localhost:5000/
  //for mobile-based applications (emulators) this will be http://10.0.2.2:5000
  static const String BASE_URL = 'http://10.0.2.2:5000';
}

class ApiService {
  static Future<dynamic> getCusotmer(String email,String password) async {
    //If the email and password are not valid , returns null
    //If the email and password are correct
    // RESPONSE IS IN THE FORMAT OF JSON :
    // {"Id": 6,
    // "FirstName": "Mariam",
    // "SecondName": "Nabil",
    // "Governorate": "Cairo",
    // "City": "Maadi",
    // "StreetName": "90st",
    // "BuildingNumber": "22",
    // "AppartmentNumber": "1",
    // "Gender": "F",
    // "PhoneNumber": 1012459878,
    // "Email": "Nor@yahoo.com",
    // "Password": "test123"}
    // }
    var queryParameters = {
      'Email': email,
      'Password': password,
    };
    var response = await http.post('${URLS.BASE_URL}/getCustomer',body: queryParameters);

    if (response.statusCode == 200) {
      print("response is 200: ok!");
      print(response.body);
      return json.decode(response.body);
    } else {
      return null;
    }
  }
  static Future<dynamic> addCustomer(customerData) async{
    final response = await http.post(Uri.encodeFull('${URLS.BASE_URL}/addCustomer'), body: customerData);
    if (response.statusCode == 200) {
      print("response is 200: ok!");
      print(response.body);
      return json.decode(response.body);
    }
    else {
      //means customer couldn't be created
      print('Signing Up Failed!');
      return null;
    }
  }
  static Future<dynamic> getEmployee(employeeData) async {
    //If the email and password are not valid , returns null
    //If the email and password are correct
    // RESPONSE IS IN THE FORMAT OF JSON :
    // {"Id": 6,
    // "FirstName": "Mariam",
    // "SecondName": "Nabil",
    // "Governorate": "Cairo",
    // "City": "Maadi",
    // "StreetName": "90st",
    // "BuildingNumber": "22",
    // "AppartmentNumber": "1",
    // "PhoneNumber": 1012459878,
    // "Email": "Nor@yahoo.com",
    // "Password": "test123",
    // "Salary": "1000",
    // "Bonus": "0"      //If DeliveryMan only
    // }
    var response = await http.post('${URLS.BASE_URL}/getEmployee',body: employeeData);

    if (response.statusCode == 200) {
      print("response is 200: ok!");
      print(response.body);
      return json.decode(response.body);
    } else {
      return null;
    }
  }
  static Future<dynamic> addEmployee(employeeData) async{
    final response = await http.post(Uri.encodeFull('${URLS.BASE_URL}/addEmployee'), body: employeeData);
    if (response.statusCode == 200) {
      print("response is 200: ok!");
      print(response.body);
      return json.decode(response.body);
    }
    else {
      //means employee couldn't be created
      print('Signing Up Failed!');
      return null;
    }
  }

}
