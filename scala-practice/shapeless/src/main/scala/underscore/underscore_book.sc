import shapeless._


case class Employee(name: String, number: Int, manager: Boolean)

case class IceCream(name: String, numCherries: Int, inCone: Boolean)

val iceCreamGen = Generic[IceCream]

val genericEmployee: String :: Int :: Boolean :: HNil =
  Generic[Employee].to(
    Employee(
      name = "Dave",
      number = 123,
      manager = false
    )
  )

val genericIceCream: String :: Int :: Boolean :: HNil =
  Generic[IceCream].to(
    IceCream(
      name = "Sundae",
      numCherries = 1,
      inCone = false
    )
  )

val repr: String :: Int :: Boolean :: HNil =
  "Hello" :: 123 :: true :: HNil

def getRepr[A](value: A)(implicit gen: Generic[A]): gen.Repr =
  gen.to(value)

case class Vec(x: Int, y: Int)

case class Rect(origin: Vec, size: Vec)

val whatType1: Int :: Int :: HNil = getRepr(Vec(1, 2))
val whatType2: Vec :: Vec :: HNil = getRepr(Rect(Vec(0, 0), Vec(5, 5)))
