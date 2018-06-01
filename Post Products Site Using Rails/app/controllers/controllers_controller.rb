class ControllersController < ApplicationController
	before_action :authenticate_login, except: [:make_user, :login, :logout, :main]
  def main
  		if(!session[:id])
			session[:id]=nil
		end
  end


  def make_user
  	user=User.new(register_params)
   	if user.valid?
      	 @user=User.create(register_params)
     	 flash[:success]="Succesfully created a new user please login"
     	 redirect_to :back
    else
      	flash[:errors]=user.errors.full_messages
      	redirect_to :back
   	end
  end

	def login
	    @user = User.find_by_email(params[:email])
	    if @user.nil?
	      flash[:errors] = ['User does not exist']
	      redirect_to :back
	    else
	      if @user.authenticate(params[:password])
	        session[:id] = @user.id
	        redirect_to '/shoes'
	      else
	        flash[:errors] = ['User Password And Email Combination Does Not Exist']
	        redirect_to :back
	      end
    	end
 	end


 	def logout
		session[:id]=nil
		redirect_to '/main'
	end


################# Start of Shoes page

def shoes
	@user=User.find(session[:id])
	@products=Product.all
end

def purchase
	product=Product.find(params[:id])
	buyer= User.find(session[:id])
	buyer_name=buyer.first_name + ' ' +buyer.last_name
	product.update(product_status: 'sold',product_buyer: buyer_name)
	product.save
	redirect_to :back

end

def dashboard
	@user=User.find(session[:id])
	@all_products=Product.all
	@products_to_sell=Product.where(user_id: session[:id], product_status: 'sale')
	@sold_products=Product.where(user_id: session[:id], product_status: 'sold')

	user_name= @user.first_name + ' ' + @user.last_name
	@bought_products=Product.where(product_buyer: user_name, product_status: 'sold')
	@user_products=Product.where(user_id: session[:id])
	@amount_sold=0
	@amount_bought=0

	@sold_products.each do |product|
		@amount_sold += product.product_amount
	end

	@bought_products.each do |product|
		@amount_bought += product.product_amount
	end
end

def remove
	product=Product.find(params[:id])
	product.destroy
	redirect_to :back
end

def create
	@user=User.find(session[:id])
	user_name= @user.first_name + ' ' + @user.last_name
	product=Product.new(product_name:params[:name], user_id: session[:id], product_amount:params[:amount], product_status: 'sale',  product_seller: user_name)
   	if product.valid?
      	 Product.create(product_name:params[:name], user_id: session[:id], product_amount:params[:amount], product_status: 'sale',  product_seller: user_name)
     	 redirect_to :back
    else
      	flash[:errors]=product.errors.full_messages
      	redirect_to :back
   	end
end
################# Private Params
  private
    def register_params
      params.require(:user).permit(:first_name, :last_name, :email,:password, :password_confirmation)
    end 

    def authenticate_login
    	if session[:id] == nil
    		flash[:errors] = ["You must be logged in to access this section"]
    		redirect_to '/main'
    	end
    end

end


