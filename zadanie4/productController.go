package main

import (
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
)

type Product struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Price int    `json:"price"`
}

var products = []Product{
	{ID: 1, Name: "Laptop", Price: 3000},
	{ID: 2, Name: "Camera", Price: 2500},
	{ID: 3, Name: "Phone", Price: 1500},
	{ID: 4, Name: "Tablet", Price: 850},
}

func main() {
	e := echo.New()

	e.GET("/products", getProducts)
	e.POST("/products", createProduct)
	e.GET("/products/:id", getProduct)
	e.PUT("/products/:id", updateProduct)
	e.DELETE("/products/:id", deleteProduct)

	e.Logger.Fatal(e.Start(":8080"))
}

func getProducts(c echo.Context) error {
	return c.JSON(http.StatusOK, products)
}

func createProduct(c echo.Context) error {
	product := new(Product)
	if err := c.Bind(product); err != nil {
		return err
	}
	products = append(products, *product)
	return c.JSON(http.StatusCreated, product)
}

func getProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	for _, p := range products {
		if p.ID == id {
			return c.JSON(http.StatusOK, p)
		}
	}
	return echo.ErrNotFound
}

func updateProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	for i := range products {
		if products[i].ID == id {
			updatedProduct := new(Product)
			if err := c.Bind(updatedProduct); err != nil {
				return err
			}
			products[i] = *updatedProduct
			return c.JSON(http.StatusOK, products[i])
		}
	}
	return echo.ErrNotFound
}

func deleteProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	for i := range products {
		if products[i].ID == id {
			products = append(products[:i], products[i+1:]...)
			return c.NoContent(http.StatusNoContent)
		}
	}
	return echo.ErrNotFound
}