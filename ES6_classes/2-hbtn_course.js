export default class HolbertonCourse {
  constructor(name, length, students) {
    this._validateAttributes(name, length, students);
    this._name = name;
    this._length = length;
    this._students = students;
  }

  _validateAttributes(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    if (typeof length !== 'number') throw new TypeError('Length must be a number');
    if (!Array.isArray(students) || students.some(student => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
  };

  get name() {
    return this._name;
  }

  set name(newName) {
    this._validateAttributes(newName, this._length, this._students);
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this._validateAttributes(this._name, newLength, this._students);
    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._validateAttributes(this._name, this._length, newStudents);
    this._students = newStudents;
  }
}
