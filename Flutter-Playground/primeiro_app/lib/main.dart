// ignore_for_file: prefer_const_constructors

import "package:flutter/material.dart";

void main() {
  runApp(MaterialApp(
      home: Scaffold(
    appBar: AppBar(
      title: Center(
          child: Text(
        "Hello Flutter!",
      )),
      backgroundColor: Colors.red[600],
    ),
    body: Center(
      child: Image(
        image: AssetImage('images/ruby.png')
      ),
    ),
  )));
}
