/**
 * @return {Generator<number>}
 */
var fibGenerator = function* () {
  let numero = 0;
  let numero_velho = 1;
  let proximo = 0;
  while (true) {
    yield proximo;

    numero += numero_velho;
    numero_velho = proximo;
    proximo = numero;
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
