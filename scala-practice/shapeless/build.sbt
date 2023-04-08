ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.5"


lazy val root = (project in file("."))
  .settings(
    name := "shapeless"
  )

libraryDependencies ++= Seq(
  "com.chuusai" %% "shapeless" % "2.3.3"
)
