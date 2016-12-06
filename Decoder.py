import numpy
import random
import work_with_matrix


class DecodeASecret:
    def __init__(self, vectors, lst_of_teachers):
        self.vectors = vectors
        self.lst_of_teachers = lst_of_teachers

    def decode(self):
        code = []
        for letter, teacher_1 in zip(self.vectors, self.lst_of_teachers):
            tmp_matrix = []
            vector = []
            for teacher in self.choose_teachers():
                tmp_matrix.extend(letter[teacher])
                vector.extend(teacher_1[teacher - 1].get_code())

            ans = self.get_value(work_with_matrix.main(tmp_matrix, vector)[0])
            code.append([numpy.array(ans).dot(letter[0][0]), numpy.array(ans).dot(letter[0][1])]) #Перевір які вектори множаться.
        print(code, "CODE")

    def choose_teachers(self):
        tmp = set()
        while len(tmp) != 3:
            tmp.add(random.randint(1, 4))
        return tmp

    def get_value(self, matrix):
        return [line[-1] for line in matrix]

    def decode_one_pair_of_bits(self, vectors, lst_of_teachers):
        key = self.get_key_from_teachers(vectors[1:4], lst_of_teachers[0:3])
        print(key, "KEY")
        b1, b2 = numpy.array(vectors[0][0]).dot(numpy.array(key)), numpy.array(vectors[0][1]).dot(numpy.array(key))

    def get_key_from_teachers(self, vectors, teachers):
        tmp_matrix = []
        augmented_side = []
        for pair, teacher in zip(vectors, teachers):
            tmp_matrix.extend(pair)
            augmented_side.extend(teacher.get_code())
        return self.get_value(work_with_matrix.main(tmp_matrix, augmented_side)[0])
