data "aws_iam_role" "existing_role" {
  name = "role-para-criacao-role-pode-ser-apagada" # Nome da role existente
}

resource "aws_lambda_function" "example_lambda" {
  function_name = "lambda-reprocessamento-glues"
  runtime       = "python3.12"
  handler       = "lambda_function.lambda_handler"
  role          = data.aws_iam_role.existing_role.arn # Role existente
  filename      = "lambda.zip" # Caminho do zip da Lambda
  source_code_hash = filebase64sha256("lambda.zip")
  environment {
    variables = {
      BUCKET_NAME = "meu-bucket"
    }
  }
}
