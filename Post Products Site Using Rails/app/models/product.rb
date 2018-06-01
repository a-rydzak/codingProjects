class Product < ActiveRecord::Base
  belongs_to :user
  validates :product_name, :product_amount, presence: true 
  validates :product_name, length: { in: 5..20 }
end
