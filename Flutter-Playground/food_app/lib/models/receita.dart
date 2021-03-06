// ignore_for_file: prefer_collection_literals, unnecessary_new, unnecessary_this

class Receita {
  late String titulo;
  late String foto;
  late String porcoes;
  late String tempoPreparo;
  late String ingredientes;
  late String modoPreparo;

  Receita(
      {required this.titulo,
      required this.foto,
      required this.porcoes,
      required this.tempoPreparo,
      required this.ingredientes,
      required this.modoPreparo});

  Receita.fromJson(Map<String, dynamic> json) {
    titulo = json['titulo'];
    foto = json['foto'];
    porcoes = json['porcoes'];
    tempoPreparo = json['tempo_preparo'];
    ingredientes = json['ingredientes'];
    modoPreparo = json['modo_preparo'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['titulo'] = this.titulo;
    data['foto'] = this.foto;
    data['porcoes'] = this.porcoes;
    data['tempo_preparo'] = this.tempoPreparo;
    data['ingredientes'] = this.ingredientes;
    data['modo_preparo'] = this.modoPreparo;
    return data;
  }
}
