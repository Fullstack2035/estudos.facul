// a) Função para trocar valores
const swap = (vetor, pos1, pos2) => {
    [vetor[pos1], vetor[pos2]] = [vetor[pos2], vetor[pos1]];
};

// b) Função para embaralhar o vetor
const shuffle = (vetor, trocas) => {
    let tamanho = vetor.length;
    for (let i = 0; i < trocas; i++) {
        let pos1 = Math.floor(Math.random() * tamanho);
        let pos2 = Math.floor(Math.random() * tamanho);
        swap(vetor, pos1, pos2);
    }
};

// c) Função Bubble Sort
const bubble_sort = (vetor) => {
    let tamanho = vetor.length;
    for (let i = 0; i < tamanho - 1; i++) {
        for (let j = 0; j < tamanho - i - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                swap(vetor, j, j + 1);
            }
        }
    }
    return vetor;
};

// d) Função Selection Sort
const selection_sort = (vetor) => {
    let tamanho = vetor.length;
    for (let i = 0; i < tamanho - 1; i++) {
        let min_idx = i;
        for (let j = i + 1; j < tamanho; j++) {
            if (vetor[j] < vetor[min_idx]) {
                min_idx = j;
            }
        }
        swap(vetor, i, min_idx);
    }
    return vetor;
};

// e) Função Quick Sort
const quick_sort = (vetor, inicio, fim) => {
    if (inicio < fim) {
        let pivotIndex = particionamento(vetor, inicio, fim);
        quick_sort(vetor, inicio, pivotIndex - 1);
        quick_sort(vetor, pivotIndex + 1, fim);
    }
    return vetor;
};

// f) Função de particionamento (apoio a quick_sort)
const particionamento = (vetor, inicio, fim) => {
    let pivot = vetor[fim];
    let i = inicio - 1;
    for (let j = inicio; j < fim; j++) {
        if (vetor[j] <= pivot) {
            i++;
            swap(vetor, i, j);
        }
    }
    swap(vetor, i + 1, fim);
    return i + 1;
};
