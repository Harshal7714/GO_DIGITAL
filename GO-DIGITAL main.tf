provider "aws" {
  region = "us-east-1"
}


resource "aws_s3_bucket" "Harshal_bucket" {
  bucket = "GO-DIGITAL-bucket"  

resource "aws_db_instance" "Go_instance" {
  identifier        = "my-Go-instance"
  allocated_storage = 20
  storage_type      = "gp2"
  engine            = "mysql"
  engine_version    = "5.7"
  instance_class    = "db.t3.micro"
  username          = "harshpatil1714@gmail.com"
  password          = "Hp@17147714"
}


resource "aws_ecr_repository" "Go_repository" {
  name = "my-ecr-repository"
}
