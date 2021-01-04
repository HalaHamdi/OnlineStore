import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:online_store/customer_SignUP.dart';
import 'package:online_store/customer_login.dart';
import 'package:online_store/employee_SignUp.dart';
import 'package:online_store/employee_login.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Login Demo',
      theme: ThemeData(
        //gives a theme for the whole app design
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
        inputDecorationTheme: InputDecorationTheme(
          focusedBorder: UnderlineInputBorder(
            borderSide: BorderSide(color: Colors.teal),
          )
        )
      ),
      home: WelcomePage(),
    );
  }
}

class WelcomePage extends StatefulWidget {
  @override
  _WelcomePageState createState() => _WelcomePageState();
}


class _WelcomePageState extends State<WelcomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        margin: EdgeInsets.all(40.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: EdgeInsets.all(30.0),
              width: double.infinity,
              decoration: BoxDecoration(
                color: Colors.teal,
                borderRadius: BorderRadius.circular(12.0)
              ),
              child: Column(
                children: [
                  Text("Welcome to our Online Store!",
                    style: TextStyle(
                      fontSize: 40,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,),
                  Icon(Icons.shopping_cart_outlined, size: 100, color: Colors.white,)
                ],
              )
            ),
            Container(
                padding: EdgeInsets.all(20.0),
                width: double.infinity,
                decoration: BoxDecoration(
                    color: Colors.grey[350],
                    borderRadius: BorderRadius.circular(12.0)
                ),
                child: Column(
                  children: [
                    Text("Continue As?", ),
                    RaisedButton(
                      shape: StadiumBorder(),
                        color: Colors.teal,
                        child: Text("Customer", style: TextStyle(color: Colors.white, fontSize: 20.0),),
                        onPressed: (){
                          Navigator.push(context, MaterialPageRoute(builder: (BuildContext context)=>CustomerLogin()));
                        }),
                    RaisedButton(
                        shape: StadiumBorder(),
                        color: Colors.teal,
                        child: Text("Employee", style: TextStyle(color: Colors.white, fontSize: 20.0),),
                        onPressed: (){
                          Navigator.push(context, MaterialPageRoute(builder: (BuildContext context)=>EmployeeLogin()));
                        }),
                  ],
                )
            ),
          ],
        ),
      ),
    );
  }
}
