<template>
    <section class="py-100-70 login">
        <div class="text-center mb-4">
            <h2>Welcome Please Login</h2>
        </div>
        <div class="container">
            <div class="col-md-4 offset-md-4">

                <!-- Pills content -->
                <div class="tab-content">
                    <div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
                        <form>
                            <!-- Email input -->
                            <div class="form-outline mb-4">
                                <input type="email" id="loginName" class="form-control" />
                                <label class="form-label" for="loginName">Email or username</label>
                            </div>

                            <!-- Password input -->
                            <div class="form-outline mb-4">
                                <input type="password" id="loginPassword" class="form-control" />
                                <label class="form-label" for="loginPassword">Password</label>
                            </div>

                            <!-- 2 column grid layout -->
                            <div class="row mb-4">
                                <div class="col-md-6 d-flex justify-content-center">
                                    <!-- Checkbox -->
                                    <div class="form-check mb-3 mb-md-0">
                                        <input class="form-check-input" type="checkbox" value="" id="loginCheck"
                                            checked />
                                        <label class="form-check-label" for="loginCheck"> Remember me </label>
                                    </div>
                                </div>

                                <div class="col-md-6 d-flex justify-content-center">
                                    <!-- Simple link -->
                                    <a href="#!">Forgot password?</a>
                                </div>
                            </div>

                            <!-- Submit button -->
                            <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>

                            <!-- Register buttons -->
                            <div class="text-center">
                               <router-link :to="{name:'register'}" class="btn-1 btn-5 sec-btn">Not a member? Register</router-link>
                            </div>
                        </form>
                    </div>
                </div>
                <!-- Pills content -->
            </div>
        </div>
    </section>
</template>
