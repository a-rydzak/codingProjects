class CreateProducts < ActiveRecord::Migration
  def change
    create_table :products do |t|
      t.string :product_name
      t.references :user, index: true, foreign_key: true
      t.integer :product_amount
      t.string :product_status
      t.string :product_buyer
      t.string :product_seller

      t.timestamps null: false
    end
  end
end
