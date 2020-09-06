class modelHandler {
    constructor() {
        //Set up neural network options
        const options = {
            // task: 'regression',
            task: 'classification',
            debug: true
        }
        // initialize neuralNetwork
        const nn = ml5.neuralNetwork(options);
    }

    createDataListFromArray(input, ignoreFirst) {
        let result = [];
        ignoreFirst = (ignoreFirst || false);
        let FirstIndex = 0
        if (ignoreFirst) { FirstIndex = 1 }
        for (let i = FirstIndex; i < input.length; i++) {
            let row = input[i];
            let data = {
                r: row[0],
                g: row[1],
                b: row[2],
                color: row[3]
            }
            result.push(data);
        }
        return result
    }

    train(data) {
        // add data to the neural network
        data.forEach(item => {
            const inputs = {
                r: item.r,
                g: item.g,
                b: item.b
            };
            const output = {
                color: item.color
            };

            this.nn.addData(inputs, output);
        });

        this.nn.normalizeData();

        // train your neural network
        const trainingOptions = {
            epochs: 32,
            batchSize: 12
        }

        this.nn.train(trainingOptions, finishedTraining);
    }
}