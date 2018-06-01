Rails.application.routes.draw do

  get 'main' => 'controllers#main'

 post 'make_user' => 'controllers#make_user'
  post 'login'=> 'controllers#login'
  get 'logout'=> 'controllers#logout'
  get 'shoes'=> 'controllers#shoes'

  get 'purchase/:id'=> 'controllers#purchase'
  get 'dashboard/:id' => 'controllers#dashboard'
  get 'remove/:id' => 'controllers#remove'
  post 'create/:id' => 'controllers#create'
  # post 'create_event/:id'=> 'controllers#create_event'
  # get 'events'=> 'controllers#events'
  # get 'join_event/:id' => 'controllers#join_event'
  # get 'logout'=> 'controllers#logout'
  # get 'cancel_event/:id'=> 'controllers#cancel_event'
  # get 'event/:id' => 'controllers#event'
  # post 'make_comment/:id' => 'controllers#make_comment'
  # get 'event_dashboard' => 'controllers#event_dashboard'
  # get 'destroy_event/:id' => 'controllers#destroy_event'
  # get 'edit_profile/:id' => 'controllers#edit_profile'
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
