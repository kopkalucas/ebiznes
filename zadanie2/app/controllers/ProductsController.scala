package controllers


import javax.inject._
import play.api.mvc._
import play.api.libs.json._


@Singleton
class ProductController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {

  case class Product(id: Long, name: String, price: Double)

  implicit val productReads: Reads[Product] = Json.reads[Product]


  var products = Seq(
    Product(1, "Laptop", 999.99),
    Product(2, "Smartphone", 599.99),
    Product(3, "Tablet", 399.99)
  )


  implicit val productWrites = new Writes[Product] {
    def writes(product: Product) = Json.obj(
      "id" -> product.id,
      "name" -> product.name,
      "price" -> product.price
    )
  }


  def getProducts = Action {
    Ok(Json.toJson(products))
  }


  def getProductById(id: Long) = Action {
    products.find(_.id == id) match {
      case Some(product) => Ok(Json.toJson(product))
      case None => NotFound("Product not found")
    }
  }

  def addProduct = Action(parse.json) { request =>
    request.body.validate[Product].map { product =>
      products :+= product.copy(id = products.length + 1)
      Ok("Product added successfully")
    }.getOrElse {
      BadRequest("Invalid product format")
    }
  }
}