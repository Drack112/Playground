// ignore_for_file: prefer_const_constructors_in_immutables, unnecessary_new, prefer_const_constructors, unnecessary_null_comparison, avoid_redundant_argument_values

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:food_app/models/receita.dart';
import "package:food_app/screens/details/details.dart";

class Home extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => new HomeState();
}

class HomeState extends State<Home> {
  @override
  Widget build(BuildContext context) {
    return _construirHome();
  }

  Widget _construirHome() {
    return Scaffold(
        body: SizedBox(
            child: FutureBuilder(
          future:
              DefaultAssetBundle.of(context).loadString('assets/receitas.json'),
          builder: (context, snapshot) {
            List<dynamic> receitas = json.decode(snapshot.data.toString());

            return ListView.builder(
              itemBuilder: (BuildContext context, int index) {
                Receita receita = Receita.fromJson(receitas[index]);
                return _construirCard(receita);
              },
              itemCount: receitas == null ? 0 : receitas.length,
            );
          },
        )),
        appBar: AppBar(title: Text("Cozinhando em Casa!")));
  }

  Widget _construirCard(receita) {
    return GestureDetector(
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => Details(
                        receita: receita,
                        key: null,
                      )));
        },
        child: Card(
            margin: EdgeInsets.all(16),
            child: Column(
              children: <Widget>[
                Stack(
                  children: <Widget>[
                    _construirImagemCard(receita.foto),
                    _construirImagemGradienteCard(),
                    _construirTituloCard(receita.titulo)
                  ],
                ),
              ],
            )));
  }

  Widget _construirImagemCard(String imagem) {
    return
//      ClipRRect(
//        borderRadius: BorderRadius.all(Radius.circular(6)),
//        child:
        Image.asset(imagem, fit: BoxFit.fill, height: 238);
//    );
  }

  Widget _construirTituloCard(String titulo) {
    return Positioned(
        bottom: 10.0,
        left: 10.0,
        child:
            Text(titulo, style: TextStyle(color: Colors.white, fontSize: 20)));
  }

  Widget _construirImagemGradienteCard() {
    return Container(
        height: 238,
        decoration: BoxDecoration(
            gradient: LinearGradient(
                begin: FractionalOffset.topCenter,
                end: FractionalOffset.bottomCenter,
                colors: [
              Colors.transparent,
              Colors.deepOrange.withOpacity(0.7)
            ])));
  }
}
