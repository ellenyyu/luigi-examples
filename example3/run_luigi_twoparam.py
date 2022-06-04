import luigi

# testing multiple parameters - it works! 
# adapted from: https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/ 

class PrintNumbers(luigi.Task):
    start = luigi.IntParameter()
    n = luigi.IntParameter()
 
    def requires(self):
        return []
 
    def output(self):
        return luigi.LocalTarget("numbers_up_to_{}.txt".format(self.n))
 
    def run(self):
        with self.output().open('w') as f:
            for i in range(self.start, self.n+1):
                f.write("{}\n".format(i))
 
class SquaredNumbers(luigi.Task):
    start = luigi.IntParameter()
    n = luigi.IntParameter()
 
    def requires(self):
        # luigi.parameter.MissingParameterException: PrintNumbers[args=(), kwargs={'n': 18}]: requires the 'start' parameter to be set
        return [PrintNumbers(start=self.start, n=self.n)]
 
    def output(self):
        return luigi.LocalTarget("squares_up_to_{}.txt".format(self.n))
 
    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            print(fin)
            for line in fin:
                n = int(line.strip())
                print(n)
                out = n * n
                fout.write("{}:{}\n".format(n, out))
if __name__ == '__main__':
    luigi.run()

