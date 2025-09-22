//list all students
db.students.find();

//add new student
db.students.insertOne({
  studentId: "LL123",
  firstName: "Luna",
  lastName: "Lovegood",
  house: "Ravenclaw",
  mascot: "Eagle",
  dateCreated: new Date()
});

//update student
db.students.updateOne(
  { studentId: "LL123" },
  { $set: { lastName: "Aadams" } }
);

//delete student
db.students.deleteOne({ studentId: "LL123" });

//display all students by house
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "house",
      foreignField: "house",
      as: "student_docs"
    }
  }
]);

//display all students in gryffindor
db.houses.aggregate([
  {
    $match: { name: "gryffindor" }
  },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);

// by mascot
db.houses.aggregate([
  { $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "house",
      foreignField: "house",
      as: "student_docs"
    }
  }
]);
